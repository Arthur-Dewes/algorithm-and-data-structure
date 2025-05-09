package queue;
public class QueueArray<T> {
    private T[] fila;
    private int count;
    private int primeiro;
    private int ultimo;

    @SuppressWarnings("unchecked")
    public QueueArray(int tamanho) {
        fila = (T[]) new Object[tamanho];
        count = 0;
        primeiro = 0;
        ultimo = 0;
    }


    public void enqueue(T element) {
        if (count == fila.length) {
            throw new RuntimeException("A fila está cheia!");
        }
        fila[ultimo] = element;
        ultimo = (ultimo + 1) % fila.length;
        count++;
    }

    public T dequeue() {
        if (isEmpty()) {
            throw new RuntimeException("A fila está vazia!");
        }
        T element = fila[primeiro];
        fila[primeiro] = null;
        primeiro = (primeiro + 1) % fila.length;
        count--;
        return element;
    }

    public T peek() {
        if (isEmpty()) {
            throw new RuntimeException("A fila está vazia!");
        }
        return fila[primeiro];
    }

    public boolean isEmpty() {
        return count == 0;
    }

    public int size() {
        return count;
    }

    @SuppressWarnings("unchecked")
    public void clear() {
        fila = (T[]) new Object[fila.length];
        count = 0;
        primeiro = 0;
        ultimo = 0;
    }
}
