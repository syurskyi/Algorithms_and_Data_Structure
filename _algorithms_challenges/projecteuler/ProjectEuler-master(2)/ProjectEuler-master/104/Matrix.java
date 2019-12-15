import java.math.BigInteger;

public class Matrix {
	public BigInteger[][] m = new BigInteger[2][2];

	public Matrix() {
		m[0][0] = BigInteger.ONE;
		m[0][1] = BigInteger.ZERO;
		m[1][0] = BigInteger.ZERO;
		m[1][1] = BigInteger.ONE;
	}

	public Matrix(long a, long b, long c, long d) {
		m[0][0] = BigInteger.valueOf(a);
		m[0][1] = BigInteger.valueOf(b);
		m[1][0] = BigInteger.valueOf(c);
		m[1][1] = BigInteger.valueOf(d);
	}
	
	public Matrix(BigInteger a, BigInteger b, BigInteger c, BigInteger d) {
		m[0][0] = a;
		m[0][1] = b;
		m[1][0] = c;
		m[1][1] = d;
	}

	Matrix multiply(Matrix other) {
		return new Matrix(
				(m[0][0].multiply(other.m[0][0])).add((m[0][1].multiply(other.m[1][0]))),
				(m[0][0].multiply(other.m[0][1])).add((m[0][1].multiply(other.m[1][1]))),
				(m[1][0].multiply(other.m[0][0])).add((m[1][1].multiply(other.m[1][0]))),
				(m[1][0].multiply(other.m[0][1])).add((m[1][1].multiply(other.m[1][1]))));
	}

	Matrix pow(long n) {
		Matrix rv = new Matrix();
		Matrix temp = new Matrix(m[0][0], m[0][1], m[1][0], m[1][1]);
		for (; n > 0; n >>= 1) {
			if ((n & 1) == 1) {
				rv = rv.multiply(temp);
			}
			temp = temp.multiply(temp);
		}
		return rv;
	}
}
