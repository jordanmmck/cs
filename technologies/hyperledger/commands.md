docker ps --format '{{.Names}}'
docker logs -f cli
docker logs dev-peer0.org2.example.com-mycc-1.0

docker rm -f $(docker ps -aq)
docker rmi -f $(docker images | grep fabcar | awk '{print $3}')

peer channel join -b mychannel.block
peer channel getinfo -c mychannel

// doesn't seem to work anywhere
peer channel fetch newest

## List all channels that peer belongs to
peer channel list

## Install chaincode
docker exec -e "CORE_PEER_LOCALMSPID=Org1MSP" -e "CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp" cli peer chaincode install -n fabcar -v 1.0 -p "$CC_SRC_PATH" -l "$CC_RUNTIME_LANGUAGE"

```
docker exec cli peer chaincode install -n fabcar -v 1.5 -p "/opt/gopath/src/github.com/fabcar/javascript" -l "node"
```

* Grabs from local? Not sure how it knows where to look. Can be invoked from anywhere.

## Instantiate chaincode

docker exec -e "CORE_PEER_LOCALMSPID=Org1MSP" -e "CORE_PEER_MSPCONFIGPATH=/opt/gopath/src/github.com/hyperledger/fabric/peer/crypto/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp" cli peer chaincode instantiate -o orderer.example.com:7050 -C mychannel -n fabcar -l "$CC_RUNTIME_LANGUAGE" -v 1.0 -c '{"Args":[]}' -P "OR ('Org1MSP.member','Org2MSP.member')"

```
docker exec cli peer chaincode instantiate -o orderer.example.com:7050 -C mychannel -n fabcar -l "node" -v 1.0 -c '{"Args":[]}' -P "OR ('Org1MSP.member','Org2MSP.member')"
```

## Upgrade chaincode

```
docker exec cli peer chaincode upgrade -o orderer.example.com:7050 -C mychannel -n fabcar -l "node" -v 1.5 -c '{"Args":[]}' -P "OR ('Org1MSP.member','Org2MSP.member')"
```
