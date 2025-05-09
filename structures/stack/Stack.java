package stack;
import java.util.NoSuchElementException;

public class Stack {

    private class Node {
        public Integer element;
        public Node next;

        public Node(Integer element) {
            this.element = element;
            next = null;
        }
    }

    private Node top;
    private int capacity;

    public Stack() {
        top = null;
        capacity = 0;
    }

    public void push(int value) {
        Node n = new Node(value);
        n.next = top;
        top = n;
        capacity++;
    }

    public void pop() {
        if (isEmpty()) {
            throw new NoSuchElementException("Stack is empty!");
        }
        top = top.next;
        capacity--;
    }

    public int peek() {
        if (isEmpty()) {
            throw new NoSuchElementException("Stack is empty!");
        }
        return top.element;
    }

    public int size() {
        return capacity;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public void clear() {
        top = null;
        capacity = 0;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        
        if (capacity == 0) {
            sb.append("Stack: No Element");
        } else {
            Node current = top;
            sb.append("Stack: ");
            while (current != null) {
                sb.append(current.element).append(" ");
                current = current.next;
            }
        }
        
        return sb.toString();
    }
    
}
