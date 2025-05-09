package linkedlist;
public class linkedList {

    private class Node {
        public Integer element;
        public Node next;

        public Node(Integer element) {
            this.element = element;
            next = null;
        }

        @SuppressWarnings("unused")
        public Node(Integer element, Node next) {
            this.element = element;
            this.next = next;
        }        
    }

    private Node head;
    private Node tail;
    private int count;

    public linkedList() {
        head = null;
        tail = null;
        count = 0;
    }

    public boolean isEmpty() {
        return (head == null);
    }


    public int size() {
        return count;
    }

    public void clear() {
        head = null;
        tail = null;
        count = 0;
    }    

    public void add(Integer element)  {
        Node n = new Node(element);
        if (head == null) {
            head = n;
        } else {
            tail.next = n;
        }
        tail = n;
        count++;
    }

    public Integer get(int index) { //O(n)
        if ((index < 0) || (index >= count)) 
            throw new IndexOutOfBoundsException();

        if (index == count-1)
            return tail.element;

        Node aux = head;
        for (int c = 0;c < index; c++)
            aux = aux.next;
        
        return aux.element;
    }

    public boolean contains(Integer element) { //O(n)
        Node aux = head;
        while(aux != null) {
            if (aux.element.equals(element))
                return true;
            aux = aux.next;
        }
        return false;
    }

    public String toString() {
        StringBuilder s = new StringBuilder();

        Node aux = head;

        while (aux != null) {
            s.append(aux.element.toString());
            s.append("\n");
            aux = aux.next;
        }

        return s.toString();
    }    

    public boolean remove(Integer element) {
        if (count == 0)
            return false;

        if (element.equals(head.element)) {
            if (count == 1) { 
                tail = null;
            }
            head = head.next;
            count--;
            return true;
        }

        Node ant = head; 
        Node aux = head.next;

        for (int i=1; i<count; i++) {
            if (aux.element.equals(element)) { 
                if (aux == tail) { //remocao do ultimo
                    tail = ant;
                    tail.next = null;
                }
                else {
                    ant.next = aux.next;
                }
                count--;
                return true;
            }
            aux = aux.next;
            ant = ant.next;
        }   
        // Se nao removeu
        return false;
    }

    public void insert(Integer element, int pos) {
        if (pos < 0 || pos > count) { 
            throw new IndexOutOfBoundsException("Posição inválida");
        }
    
        Node n = new Node(element);
    
        if (pos == 0) {
            n.next = head;
            head = n;
            if (count == 0) {
                tail = n;
            }
        } else {
            Node atual = head;
            for (int i = 0; i < pos - 1; i++) {
                atual = atual.next;
            }
            n.next = atual.next;
            atual.next = n;
            if (n.next == null) {
                tail = n;
            }
        }
    
        count++; 
    }

    public void set(Integer element, int pos){
        Node n = new Node(element);

        if (pos < 0 || pos >= count)
            throw new IndexOutOfBoundsException();

        if (pos == 0)
            head = n;

        if (pos == count - 1)
            tail = n;

        Node atual = head;
        int i = 0;
        while (i != pos){
            atual = atual.next;
            i++;
        }
        atual.element = n.element;

        
    }

    public void remove_at(int pos){
        if (pos < 0 || pos >= count)
            throw new IndexOutOfBoundsException();

        if (pos == 0)
            head = head.next;

        Node atual = head;
        for (int i = 0; i < pos - 1; i++){
            atual = atual.next;
        }

        atual.next = atual.next.next;
    }
    
    public int indexOf(Integer element){
        Node atual = head;
        int i = 0;
        while (atual != null){
            if (atual.element == element)
                return i;
            atual = atual.next;
            i++;
        }
        return -1;
    }

}

