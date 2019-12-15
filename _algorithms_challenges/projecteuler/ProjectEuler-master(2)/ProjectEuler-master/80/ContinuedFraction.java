import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Iterator;

public class ContinuedFraction {
	public void setContinuedFraction(long n) {
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
	
	public void setFraction(int places) {
		Long[] cycleArray = cycle.toArray(new Long[0]);
		int length = cycleArray.length;
		BigInteger prevNumerator = BigInteger.valueOf(integer);
		BigInteger prevDenominator = BigInteger.ONE;
		BigInteger currNumerator = BigInteger.valueOf(integer)
				.multiply(BigInteger.valueOf(cycleArray[0])).add(BigInteger.ONE);
		BigInteger currDenominator = BigInteger.valueOf(cycleArray[0]);
		
		for (int k = 2; ; k++) {
			BigInteger nextNumerator = BigInteger.valueOf(cycleArray[(k-1) % length])
					.multiply(currNumerator).add(prevNumerator);
			BigInteger nextDenominator = BigInteger.valueOf(cycleArray[(k-1) % length])
					.multiply(currDenominator).add(prevDenominator);
			BigInteger inversedEpsilon = currDenominator.multiply(nextDenominator);

			if (inversedEpsilon.toString().length() > places) {
				numerator = currNumerator;
				denominator = currDenominator;
				break;
			}
			
			prevNumerator = currNumerator;
			currNumerator = nextNumerator;
			prevDenominator = currDenominator;
			currDenominator = nextDenominator;
		}
	}
	
	public long getDecimalDigitSum(int places) {
		setFraction(places + 30);
		String digitString = numerator.multiply(BigInteger.valueOf(10).pow(places))
				.divide(denominator).toString();
		long sum = 0;
		for (int i = 0; i < places; i++) {
			sum += digitString.charAt(i) - '0';
		}
		return sum;
	}
	
	public void debug() {
		System.out.printf("Sqrt[%d] = [%d;(", n, integer);
		Iterator<Long> it = cycle.iterator();
		int length = cycle.size();
		int count = 0;
		while(it.hasNext()) {
		    System.out.printf("%d", it.next());
		    count++;
		    if (count != length) {
		    	System.out.print(",");
		    }
		}
		System.out.printf(")], period = %d\n", length);
	}
	
	private long n;
	
	private long integer;
	
	private BigInteger numerator;
	
	private BigInteger denominator;
	
	private ArrayList<Long> cycle;
}
