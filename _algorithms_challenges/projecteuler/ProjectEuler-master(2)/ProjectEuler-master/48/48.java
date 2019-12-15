import java.math.BigInteger;

public class Main {
	public static void main(String[] args) {
		BigInteger m = BigInteger.valueOf(10).pow(10);
		
		BigInteger sum = BigInteger.ZERO;
		for (int i = 1; i <= 1000; i++) {
			sum = sum.add(BigInteger.valueOf(i).modPow(BigInteger.valueOf(i), m));
			sum = sum.mod(m);
		}
		
		System.out.println(sum);
	}
}
