import java.math.BigInteger;

public class ModMatrix {
	public BigInteger[][] m = new BigInteger[2][2];

	public ModMatrix(BigInteger mod) {
		m[0][0] = BigInteger.ONE;
		m[0][1] = BigInteger.ZERO;
		m[1][0] = BigInteger.ZERO;
		m[1][1] = BigInteger.ONE;
		M = mod;
	}

	public ModMatrix(long a, long b, long c, long d, BigInteger mod) {
		m[0][0] = BigInteger.valueOf(a);
		m[0][1] = BigInteger.valueOf(b);
		m[1][0] = BigInteger.valueOf(c);
		m[1][1] = BigInteger.valueOf(d);
		M = mod;
	}
	
	public ModMatrix(BigInteger a, BigInteger b, BigInteger c, BigInteger d, BigInteger mod) {
		m[0][0] = a;
		m[0][1] = b;
		m[1][0] = c;
		m[1][1] = d;
		M = mod;
	}

	ModMatrix multiply(ModMatrix other) {
		return new ModMatrix(
				(m[0][0].multiply(other.m[0][0])).add((m[0][1].multiply(other.m[1][0]))).mod(M),
				(m[0][0].multiply(other.m[0][1])).add((m[0][1].multiply(other.m[1][1]))).mod(M),
				(m[1][0].multiply(other.m[0][0])).add((m[1][1].multiply(other.m[1][0]))).mod(M),
				(m[1][0].multiply(other.m[0][1])).add((m[1][1].multiply(other.m[1][1]))).mod(M), M);
	}

	ModMatrix pow(BigInteger n) {
		ModMatrix rv = new ModMatrix(M);
		ModMatrix temp = new ModMatrix(m[0][0], m[0][1], m[1][0], m[1][1], M);
		for (; n.compareTo(BigInteger.ZERO) > 0; n = n.shiftRight(1)) {
			if (n.testBit(0)) {
				rv = rv.multiply(temp);
			}
			temp = temp.multiply(temp);
		}
		return rv;
	}
	
	private BigInteger M;
}
