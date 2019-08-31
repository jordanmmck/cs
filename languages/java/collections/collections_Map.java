import java.io.*;
import java.util.*;
import java.math.*;

public class collections_Map{
    
    public static String generateString(Random rng, String characters, int length){
        char[] text = new char[length];
        for(int i = 0; i < length; i++)
            text[i] = characters.charAt(rng.nextInt(characters.length()));
        return new String(text);
    }

    public static void main(String args[]) throws Exception{
        Random rand = new Random();

        Map<Integer,String> mapA = new Hashtable<Integer,String>();
        Map<Integer,String> mapB = new HashMap<Integer,String>();
        Map<Integer,String> mapC = new LinkedHashMap<Integer,String>();
        SortedMap<Integer,String> mapD = new TreeMap<Integer,String>();
        NavigableMap<String, String> mapE = new TreeMap<String, String>();
        
        // fill map with number-string key-value pairs
        // re-inserting strings using the existing keys will overwrite!
        // the keys are a SET. No duplicates
        for(int i=0; i<5; i++)
            mapA.put(rand.nextInt(100),generateString(rand,"abcdefghi",5));

        // print key-value pairs as dictionary
        System.out.println(mapA);
        // print values
        System.out.println(mapA.values());
        // print keys
        System.out.println(mapA.keySet());
        // sort keys and print
        TreeSet sortedMapA = new TreeSet<Integer>(mapA.keySet());
        System.out.println(sortedMapA);

        // for detecting duplicates
        for (int i=0; i<5; i++) {
            int val = cin.nextInt();
            if(map.containsKey(val))
                map.put(val,-1);
            else
                map.put(val,i+1);
        }


        // iterate through keys printing values
        for (Integer key : mapA.keySet())
            System.out.print(key+": "+mapA.get(key)+", ");
        System.out.println();
    }
}