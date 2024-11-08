package jvmgo.book.ch07;

/* loaded from: InvokeDemo.class */
public class InvokeDemo implements Runnable {
    public static void main(String[] args) {
        new InvokeDemo().test();
    }

    public void test() {
        staticMethod();
        InvokeDemo demo = new InvokeDemo();
        demo.instanceMethod();
        super.equals(null);
        run();
        demo.run();
    }

    public static void staticMethod() {
    }

    private void instanceMethod() {
    }

    @Override // java.lang.Runnable
    public void run() {
    }
}