import java.util.HashSet;

public class Main {
	public static void main(String[] args) {
		initSquares();
		
		long rv = 0;
		for (long n = 1; n <= 100; n++) {
			ContinuedFraction fraction = new ContinuedFraction();
			if (!squares.contains(n)) {
				fraction.setContinuedFraction(n);
				rv += fraction.getDecimalDigitSum(100);
			}
		}
		System.out.println(rv);
	}	
	
	private static void initSquares() {
		for (long n = 1; n <= 10; n++) {
			squares.add(n*n);
		}
	}
	
	private static HashSet<Long> squares = new HashSet<Long>(); 
}
