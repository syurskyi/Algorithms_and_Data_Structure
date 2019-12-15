import java.math.BigInteger;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) {
		initSquares();
		
		BigInteger max = BigInteger.ZERO;
		long maxAtD = 1;
		for (long d = 1; d <= 1000; d++) {
			PellEquation equation = new PellEquation();
			if (!squares.contains(d)) {
				equation.solve(d);
				if (equation.getX().compareTo(max) > 0) {
					max = equation.getX();
					maxAtD = d;
				}
			}
		}
		System.out.println(maxAtD);
	}	
	
	private static void initSquares() {
		for (long n = 1; n <= 32; n++) {
			squares.add(n*n);
		}
	}
	
	private static HashSet<Long> squares = new HashSet<Long>(); 
}
