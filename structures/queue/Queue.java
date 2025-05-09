package queue;
public class Queue<T> {
    private class Node {
        T element;
        Node next;

        public Node(T element) {
            this.element = element;
            this.next = null;
        }
    }

    private Node head;
    private Node tail;
    private int count;

    public Queue() {
        head = null;
        tail = null;
        count = 0;
    }

    public void enqueue(T element) {
        Node newNode = new Node(element);
        if (tail != null) {
            tail.next = newNode;
        }
        tail = newNode;
        if (head == null) {
            head = tail;
        }
        count++;
    }

    public T dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("A fila está vazia!");
        }
        T element = head.element;
        head = head.next;
        if (head == null) {
            tail = null;
        }
        count--;
        return element;
    }

    public T peek() {
        if (isEmpty()) {
            throw new RuntimeException("A fila está vazia!");
        }
        return head.element;
    }

    public boolean isEmpty() {
        return count == 0;
    }

    public int size() {
        return count;
    }

    public void clear() {
        head = null;
        tail = null;
        count = 0;
    }
}

