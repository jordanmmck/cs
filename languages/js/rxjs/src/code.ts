import { Observable, fromEvent } from 'rxjs';

const addItem = (val: any) => {
  const node = document.createElement('li');
  const textnode = document.createTextNode(val);
  node.appendChild(textnode);
  document.getElementById('output').appendChild(node);
};

const observable = Observable.create((observer: any) => {
  observer.next('1');
  observer.next('2');
  observer.complete();
  observer.next('3');
});

observable.subscribe(
  (x: any) => addItem(x),
  (error: any) => addItem(error),
  () => addItem('completed')
);
