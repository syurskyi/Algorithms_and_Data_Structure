/*********************************************************
 Пример использования:
		OList<Integer> l = new OList<Integer>();
		for(int i=0; i<10; i++)
			l.add(i*i);
		
		OList<Integer>.ListItem<Integer> li = l.head();
		while (li != null) {
			System.out.println(li.get());
			li = li.getNext();
		}
*********************************************************/

package BaseTypes;

public class OList<T> {
	
	@SuppressWarnings("hiding")
	class ListItem<T> {
		T _item;
		ListItem<T> _next;
		
		ListItem(T item) {
			_item = item;
			_next = null;
		}
		
		T get() {
			return _item;
		}
		
		void setNext(ListItem<T> item) {
			_next = item;
		}
		ListItem<T> getNext() {
			return _next;
		}
	}
	
	ListItem<T> _head;
	ListItem<T> _tail;
	
	OList() {
		_head = null;
		_tail = null;
	}
	
	ListItem<T> head() {
		return _head;
	}
		
	void add(T item) {
		ListItem<T> li = new ListItem<T>(item); 
		if (_head == null) {
			_head = li;
			_tail = li;
		}
		else {
			_tail.setNext(li);
			_tail = li;
		}
	}
}
