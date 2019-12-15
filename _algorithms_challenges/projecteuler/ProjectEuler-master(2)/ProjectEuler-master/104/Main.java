import java.math.BigInteger;

public class Main {
	public static void main(String[] args) {
		long prevFib = 1;
		long currFib = 1;
		long nextFib = 0;
		for (long k = 3; ; k++) {
			nextFib = (currFib + prevFib) % 1000000000;
			prevFib = currFib;
			currFib = nextFib;
			if (isPandigital(currFib)) {
				if (isPandigital(getFirstNineDigit(getFibonacci(k)))) {
					System.out.println(k);
					break;
				}
			}
		}
	}
	
	private static boolean isPandigital(long n) {
		boolean[] digit = new boolean[9];
		long d = n;
		int r = 0;
		long digitCount = 0;
		while (d > 0) {
			r = (int)(d % 10);
			if (r == 0) {
				return false;
			}
			if (digit[r-1]) {
				return false;
			}
			digit[r-1] = true;
			digitCount++;
			d /= 10;
		}
		return digitCount == 9;
	}
	
	private static long getFirstNineDigit(BigInteger n) {
		String rep = n.toString();
		if (rep.length() < 9) {
			return 0;
		}
		rep = rep.substring(0, 9);
		return Long.parseLong(rep);
	}
	
	private static BigInteger getFibonacci(long k) {
		if (k == 0) {
			return BigInteger.ZERO;
		}
		Matrix a = new Matrix(1, 1, 1, 0);
		return a.pow(k - 1).m[0][0];
	}
}
