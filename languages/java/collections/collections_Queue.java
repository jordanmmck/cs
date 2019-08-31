import java.io.*;
import java.util.*;
import java.math.*;

public class collections_Queue{
    public static void main(String args[]) throws Exception{
        
        Random rand = new Random();
        Queue<Integer> queueA = new LinkedList<Integer>();

        // enqueue
        for(int i=0; i<5; i++)
            queueA.add(rand.nextInt(100));
        System.out.println(queueA);
        
        System.out.println(queueA.remove());
        System.out.println(queueA.peek());
    }
}