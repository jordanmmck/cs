import java.io.*;
import java.util.*;
import java.math.*;

public class collections_Set{
    public static void main(String args[]) throws Exception{
        Random rand = new Random();
        
        Set<Integer> setA = new HashSet<Integer>();
        Set<Integer> setB = new TreeSet<Integer>();
        Set<Integer> setC = new LinkedHashSet<Integer>();
        Set<Character> setD = new HashSet<Character>();

        // fill set
        for(char c: "abcd12345".toCharArray())
            setD.add(c);
        for(int i=0; i<5; i++)
            setA.add(rand.nextInt(100));
        System.out.println("size: "+setA.size()+", "+setA);

        // iterate through set/list
        Iterator iterSet = setA.iterator();
        while (iterSet.hasNext()) {
            System.out.print(iterSet.next()+" ");
        }System.out.println();

        // sort the set
        TreeSet sortedSetA = new TreeSet<Integer>(setA);    
        System.out.println("sorted: "+sortedSetA);

        // set difference
        setD.removeAll(setA);
        // setD becomes union
        setD.addAll(setA);
        // setD becomes intersection
        setD.retainAll(setA);
        // true if setA is a subset of setD
        setD.containsAll(setA);

        System.out.println(sortedSetA.last());   
        // cast set to array for indexing
        Object setArr[] = sortedSetA.toArray();
        System.out.println(setArr[0]);
    }
}