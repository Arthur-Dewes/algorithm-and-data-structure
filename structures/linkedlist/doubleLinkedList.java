package linkedlist;
public class doubleLinkedList {

    private Node head;
    private Node tail;   
    private int count;

     private class Node {
        public Integer element;
        public Node next;
        public Node prev;
        public Node(Integer e) {
            element = e;
            next = null;
            prev = null;
        }
    }

    public doubleLinkedList() {
        head = new Node(null);
        tail = new Node(null);
        head.next = tail;
        tail.prev = head;
        count = 0;
    }

    public void clear() {
        head = new Node(null);
        tail = new Node(null);
        head.next = tail;
        tail.prev = head;
        count = 0;
    }    

    public int size() {
        return count;
    }

    private Node getNodeIndex(int index) {
        Node aux = null;
        
        if (index < count/2) {
            aux = head.next;
            for (int i=0; i<index; i++) {
                aux = aux.next;
            }
        }
        else {
            aux = tail.prev;
            for (int i=count-1; i>index; i--) {
                aux = aux.prev;
            }
        }
        
        return aux;
    }

    public Integer get(int index) {
        if ((index < 0) || (index >= count)) {
            throw new IndexOutOfBoundsException();
        }
        Node aux = getNodeIndex(index);
        return aux.element;
    }

    public Integer set(int index, Integer element) {
        if ((index < 0) || (index >= count)) {
            throw new IndexOutOfBoundsException();
        }
        Node aux = getNodeIndex(index);
        Integer elem = aux.element;
        aux.element = element;
        return elem;
    }

    public void add(Integer element) {
        Node n = new Node(element);

        n.prev = tail.prev;
        n.next = tail;

        tail.prev.next = n;
        tail.prev = n;

        count++;
    }

    public void add_inicio(Integer element) {
        Node n = new Node(element);

        n.prev = head;
        n.next = head.next;

        head.next = n;

        count++;
    }
    
    public boolean remove(Integer element) {
        Node aux = head.next;
        for(int i=0; i<count;i++) {
            if (aux.element.equals(element)) { 
                aux.prev.next = aux.next;
                aux.next.prev = aux.prev;
                count--;               
                return true;
            }
            aux = aux.next;
        }
        return false;	
    }

    public void imprimirReverse(){
        Node aux = tail.prev;
        for (int i = 0; i < count; i++) {
            System.out.println(aux.element);
            aux = aux.prev;
        }
    } 
    
    public boolean isEmpty() {
        return (count == 0);
    } 

    public String toString()
    {
        StringBuilder s = new StringBuilder();
        Node aux = head.next;
        for (int i = 0; i < count; i++) {
            s.append(aux.element.toString());
            s.append("\n");
            aux = aux.next;
        }
        return s.toString();
    } 
    
}
