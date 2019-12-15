import java.math.BigInteger;
import java.util.ArrayList;

public class PellEquation {
	public void solve(long n) {
		setD(n);

		BigInteger prevNumerator = BigInteger.valueOf(integer);
		BigInteger prevDenominator = BigInteger.ONE;
		if (isSolution(prevNumerator, prevDenominator)) {
			x = prevNumerator;
			y = prevDenominator;
			return;
		}
		
		Long[] cycleArray = cycle.toArray(new Long[0]);
		int length = cycleArray.length;
		BigInteger currNumerator = BigInteger.valueOf(integer)
				.multiply(BigInteger.valueOf(cycleArray[0])).add(BigInteger.ONE);
		BigInteger currDenominator = BigInteger.valueOf(cycleArray[0]);
		if (isSolution(currNumerator, currDenominator)) {
			x = currNumerator;
			y = currDenominator;
			return;
		}
		
		for (int k = 2; ; k++) {
			BigInteger nextNumerator = BigInteger.valueOf(cycleArray[(k-1) % length])
					.multiply(currNumerator).add(prevNumerator);
			BigInteger nextDenominator = BigInteger.valueOf(cycleArray[(k-1) % length])
					.multiply(currDenominator).add(prevDenominator);
		
			if (isSolution(currNumerator, currDenominator)) {
				x = currNumerator;
				y = currDenominator;
				return;
			}
			prevNumerator = currNumerator;
			currNumerator = nextNumerator;
			prevDenominator = currDenominator;
			currDenominator = nextDenominator;
		}
	}
	
	public BigInteger getX() {
		return x;
	}
	
	public BigInteger getY() {
		return y;
	}
	
	private boolean isSolution(BigInteger numerator, BigInteger denominator) {
		return numerator.pow(2).add(BigInteger.valueOf(-n).multiply(denominator.pow(2)))
				.compareTo(BigInteger.ONE) == 0;
	}
	
	private void setD(long n) {
		this.n = n;
		Fraction fraction = new Fraction(n, 1, 0, 1);
		fraction.makeProper();
		integer = fraction.getInteger();
		cycle = new ArrayList<Long>();
		ArrayList<Fraction> internalFractions = new ArrayList<Fraction>();
		while (true) {
			fraction.inverse();
			fraction.makeProper();
			if (internalFractions.contains(fraction)) {
				break;
			} else {
				internalFractions.add(new Fraction(fraction));
				cycle.add(fraction.getInteger());
			}
		}
	}
		
	private long n;
	
	private long integer;
	
	private BigInteger x;
	
	private BigInteger y;
	
	private ArrayList<Long> cycle;
}
