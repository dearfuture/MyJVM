package jvmgo.book.ch06;

/* loaded from: MyObject.class */
public class MyObject {
    public static int staticVar;
    public int instanceVar;

    public static void main(String[] args) {
        MyObject myObj = new MyObject();
        staticVar = 32768;
        int x = staticVar;
        myObj.instanceVar = x;
        int i = myObj.instanceVar;
        if (myObj instanceof MyObject) {
            System.out.println(myObj.instanceVar);
        }
    }
}