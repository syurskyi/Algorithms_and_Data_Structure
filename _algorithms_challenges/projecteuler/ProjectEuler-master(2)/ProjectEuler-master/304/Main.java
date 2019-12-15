import java.math.BigInteger;

public class Main {
	public static void main(String[] args) {
		sieve();
		BigInteger sum = BigInteger.ZERO;
		int primeCount = 0;		
		for (int i = 0; primeCount < 100000; i++) {
			if (!problemSieve[i]) {
				sum = sum.add(getFibonacci(N.add(BigInteger.valueOf(i)), M)).mod(M);
				primeCount++;
			}
		}
		System.out.println(sum);
	}
	
	private static BigInteger getFibonacci(BigInteger k, BigInteger mod) {
		if (k.compareTo(BigInteger.ZERO) == 0) {
			return BigInteger.ZERO;
		}
		ModMatrix a = new ModMatrix(1, 1, 1, 0, mod);
		return a.pow(k.add(BigInteger.valueOf(-1))).m[0][0];
	}
	
	private static void sieve() {
		boolean visited[] = new boolean[10200000];
		for (int i = 2; i < 10200000; i++) {
			if (!visited[i]) {				
				for (int j = i+i; j < 10200000; j += i) {
					visited[j] = true;
				}
				int k = (i == 2|| i == 5) ? 0 : i - N.mod(BigInteger.valueOf(i)).intValue();
				for (; k < 4000000; k += i) {
					problemSieve[k] = true;
				}
			}
		}
	}
	
	private static BigInteger N = new BigInteger("100000000000000");
	private static BigInteger M = new BigInteger("1234567891011");
	private static boolean problemSieve[] = new boolean[4000000]; 
}
