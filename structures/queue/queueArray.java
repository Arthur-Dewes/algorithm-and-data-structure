public class QueueArray<T> {
    private T[] queue;
    private int capacity;
    private int count;
    private int first;
    private int last;
    
    @SuppressWarnings("unchecked")
    public QueueArray() {
        this.capacity = 8;
        this.queue = (T[]) new Object[this.capacity];
        this.count = 0;
        this.first = 0;
        this.last = 0;
    }
    
    public void enqueue(T element) {
        if (this.count == this.capacity) {
            resize(2 * this.capacity);
        }
        this.queue[this.last] = element;
        this.last = (this.last + 1) % this.capacity;
        this.count++;
    }
    
    public T dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty!");
        }
        T element = this.queue[this.first];
        this.queue[this.first] = null;
        this.first = (this.first + 1) % this.capacity;
        this.count--;
        return element;
    }
    
    public T peek() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty!");
        }
        return this.queue[this.first];
    }
    
    public boolean isEmpty() {
        return this.count == 0;
    }
    
    public int size() {
        return this.count;
    }
    
    @SuppressWarnings("unchecked")
    public void clear() {
        this.capacity = 8;
        this.queue = (T[]) new Object[this.capacity];
        this.count = 0;
        this.first = 0;
        this.last = 0;
    }
    
    @SuppressWarnings("unchecked")
    private void resize(int newCapacity) {
        T[] newQueue = (T[]) new Object[newCapacity];
        for (int i = 0; i < this.count; i++) {
            newQueue[i] = this.queue[(this.first + i) % this.capacity];
        }
        this.queue = newQueue;
        this.first = 0;
        this.last = this.count;
        this.capacity = newCapacity;
    }
}