public class Fraction {
	public Fraction(long n, long irrationalNumerator, long rationalNumerator, long denominator) {
		this.n = n;
		this.irrationalNumerator = irrationalNumerator;
		this.rationalNumerator = rationalNumerator;
		this.denominator = denominator;
		this.integer = 0;
	}
	
	public Fraction(Fraction other) {
		this.n = other.n;
		this.irrationalNumerator = other.irrationalNumerator;
		this.rationalNumerator = other.rationalNumerator;
		this.denominator = other.denominator;
		this.integer = other.integer;
	}
	
	public long getInteger() {
		return this.integer;
	}
	
	public boolean equals(Object o) {
		Fraction other = (Fraction)o;
		return irrationalNumerator == other.irrationalNumerator 
				&& rationalNumerator == other.rationalNumerator
				&& denominator == other.denominator;
	}
	
	public void makeProper() {
		setInteger();
		rationalNumerator = rationalNumerator - denominator*integer;
	}
	
	public void inverse() {
		long t = denominator;
		denominator = irrationalNumerator*irrationalNumerator*n 
				- rationalNumerator*rationalNumerator;
		irrationalNumerator *= t;
		rationalNumerator *= -t;
		long gcd = getGCD(getGCD(irrationalNumerator, rationalNumerator), denominator);
		denominator /= gcd;
		irrationalNumerator /= gcd;
		rationalNumerator /= gcd;
	}
	
	public void debug() {
		System.out.printf(
				"%d + (%d Sqrt[%d] + %d)/%d\n", 
				integer, irrationalNumerator, n, rationalNumerator, denominator);
	}
	
	private void setInteger() {
		this.integer = 0;
		for (; irrationalNumerator*irrationalNumerator*n 
				> (denominator*integer + denominator - rationalNumerator)
				* (denominator*integer + denominator - rationalNumerator); integer++);		
	}
	
	private long getGCD(long a, long b) {
		a = Math.abs(a);
		b = Math.abs(b);
		while (b != 0) {
			long t = b;
			b = a % t;
			a = t;
		}
		return a;
	}
	
	private long n;
	private long irrationalNumerator;
	private long rationalNumerator;
	private long denominator;
	private long integer;
}
