package jvmgo.book.ch07;

/* loaded from: FibonacciTest.class */
public class FibonacciTest {
    public static void main(String[] args) {
        long x = fibonacci(30L);
        System.out.println(x);
    }

    private static long fibonacci(long n) {
        if (n <= 1) {
            return n;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}