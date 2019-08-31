import java.io.*;
import java.util.*;
import java.math.*;

public class collections_List{
    public static void main(String args[]) throws Exception{
        Random rand = new Random();

        List<Integer> listA = new ArrayList<Integer>();
        List<Integer> listB = new Vector<Integer>();
        List<Integer> listC = new LinkedList<Integer>();
    
        
        // fill lists
        for(int i=0; i<5; i++){
            listA.add(rand.nextInt(100));
            listB.add(rand.nextInt(100));
            listC.add(rand.nextInt(100));
        }

        // iterate through list
        for(int i=0; i<listA.size();i++)
            System.out.print(listA.get(i)+" ");
        System.out.println();

        // make new SET sorted
        TreeSet sortedList = new TreeSet<Integer>(listA);    
        System.out.println(sortedList);

        // sort LIST
        // reverse list
        Collections.sort(listA);
        Collections.reverse(listA);

        // binary search
        System.out.println(Collections.binarySearch(listA,1));

        // appends listA to listB
        listB.addAll(listA);

        // true if lists are disjoint
        System.out.println(Collections.disjoint(listA,listC));
       
        // replace all elements with new element
        Collections.fill(listA,111);
        System.out.println(listA);

        // freq, max, min
        System.out.println(Collections.frequency(listA,111));
        System.out.println(Collections.max(listB));
        System.out.println(Collections.min(listB));

        // replace all a with b
        Collections.replaceAll(listA,111,222);
        System.out.println(listA);
        
        // shuffle list
        Collections.sort(listB);
        System.out.println(listB);
        Collections.shuffle(listB);
        System.out.println(listB);
    }
}