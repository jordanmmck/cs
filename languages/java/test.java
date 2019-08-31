import java.util.Arrays;
import java.util.HashSet;
import java.util.TreeMap;
import java.util.Map;
import java.util.Set;

public class test {
    Map<Object,Set<Object>> C = new TreeMap<Object,Set<Object>>();
    Map<Object,Set<Object>> D = new TreeMap<Object,Set<Object>>();

    static Set<Object> varCol = new HashSet<Object>( Arrays.asList(new String[] {
        "blue", "green", "ivory", "red", "yellow" }));

    static Set<Object> varDri = new HashSet<Object>( Arrays.asList(new String[] {
        "coffee", "milk", "orange-juice", "tea", "water" }));

    public static void printSet(Set<Object> S){
        for(Object s: S)
            System.out.println(s);
    }

    public static void main(String[] args) throws Exception {
        Integer[] domain = {1,2,3,4,5};
        // printSet(varCol);
        String s = "";
        s += "asdfas";
        System.out.println(s);

    }
}
