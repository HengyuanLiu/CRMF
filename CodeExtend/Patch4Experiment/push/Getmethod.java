package push;

import java.lang.reflect.Method;
// import java.util.*;

public class Getmethod {
   public static void main(String[] args) {
       // Scanner sc = new Scanner(System.in);
       // String str = sc.next();
       getMethodInfo(args[0]);//com.google.debugging.sourcemap.SourceMapSupplier
   }

   /**
    * 传入全类名获得对应类中所有方法名和参数名
    */
   @SuppressWarnings("rawtypes")
   private static void getMethodInfo(String pkgName) {
       try {
           Class clazz = Class.forName(pkgName);
           Method[] methods = clazz.getMethods();
           String strName = clazz.getName();
           // System.out.println(strName);
           for (Method method : methods) {
               String methodName = method.getName();
               System.out.println(strName + "." + methodName);
               // Class<?>[] parameterTypes = method.getParameterTypes();
               // for (Class<?> clas : parameterTypes) {
               //     String parameterName = clas.getName();
               //     System.out.println("Arg Type:" + parameterName);
               // }
               // System.out.println("*****************************");
           }
       } catch (ClassNotFoundException e) {
           e.printStackTrace();
       }
   }
}