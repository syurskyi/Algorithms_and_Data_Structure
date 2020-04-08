/*********************************************************
 Пример использования:
 
 		DArray<Integer> a = new DArray<Integer>();
		
		Date start = new Date();
		for(int i=0; i<10; i++)
			a.add(i,i*i);

		for(int i=0; i<10; i++)
			System.out.println(a.get(i));
 *********************************************************/

package BaseTypes;

class DArray<T> {
	Object[] _arr;
	
	DArray() {
	}
	
	@SuppressWarnings("unchecked")	
	T get(int index) {
		return (T)_arr[index];
	}
	
	private void relocate(int newsize, int index) {
		Object[] tmp = new Object[newsize];
		
		if (_arr != null)
			for(int i=0; i < _arr.length; i++)
				if (i<index)
					tmp[i] = _arr[i];
				else
					tmp[i+1] = _arr[i];
		_arr = tmp;
	}
	
	void add(int index, T element) {
		if (_arr == null || _arr.length <= index) 
			relocate(index+1, index);
		_arr[index] = (Object)element;
	}
	
	void set(int index, T element) {
		_arr[index] = (Object)element;
	}
	
	int size( ) {
		return _arr.length;
	}
}
