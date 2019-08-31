import java.io.*;
import java.util.*;
import java.math.*;

public class string {
    public static void main(String[] args) throws Exception{
        String s1 = "jordan";
        char data[] = {'a','b','c'};
        String s2 = new String(data);

        // comparing
        System.out.println(s2.length());
        System.out.println(s1.equals(s2));
        System.out.println(s1.compareTo(s2));

        // concat
        System.out.println(s1+s2+"!");
        String s3=s1.concat(s2);
        System.out.println(s3);

        // find stuff
        System.out.println(s1.charAt(2));
        System.out.println(s3.endsWith("bc"));
        System.out.println(s3.indexOf('a',5));
        System.out.println(s3.lastIndexOf('a',5));
        System.out.println(s3.isEmpty());
        System.out.println(s3.replace('a','z'));

        // replace stuff
        String set="[1, 2, 3, 4]";
        System.out.println(set.toString().replaceAll("\\[|\\]|\\,|\\ ",""));

        // string split, string array
        String s4="abc def jjj zzx";
        String strArr[]=s4.split(" ");

        // trim
        String s5=" zxy   ";
        System.out.println(s5.trim());

        // string builder
        StringBuilder sb = new StringBuilder("Mat");
        sb.append(" ");
        sb.append("Bank");

        // oops
        int i = sb.indexOf("k");
        sb.insert(i, 'i'); // character
        String mb = sb.toString();
        // result = "Mat Banik"
    }
}
