interface Calculator {
    void calculateResult(int x, int y, CalculatorCallback callback);
}
interface CalculatorCallback {
      void onResult(int result); 
}
  
  public class CallBack {
    public static void main(String[] args) {
      Calculator calc = new CalculatorImpl();
      int a = 5;
      int b = 6;

      System.out.println("Main thread: " + Thread.currentThread().getId());
  
      calc.calculateResult(a, b, new CalculatorCallback() {
        public void onResult(int result) {
        System.out.println("Callback thread: " + Thread.currentThread().getId());
          // This is the callback function
          System.out.println("Result: " + result);  
        }
      });
      
      // Main thread continues executing
      System.out.println("Callback will execute later");
    }
  }
  
  class CalculatorImpl implements Calculator {
  
    public void calculateResult(int x, int y, CalculatorCallback callback) {
      // Executes lengthy calculation
      int result = x + y;
      
      // Callback is invoked after calculation is done
      callback.onResult(result);
    }
  }