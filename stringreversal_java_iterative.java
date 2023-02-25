import java.util.*;
public class MyClass {
    public static void main(String args[]) {
        long start = System.currentTimeMillis();
        Scanner sc= new Scanner(System.in);
        String s=sc.nextLine();
        int l=s.length();
        for(int i=l-1;i>=0;i--)
        {
            System.out.print(s.charAt(i));
        }
        long end = System.currentTimeMillis();
        System.out.println();
        System.out.println(end-start);
    }
}
