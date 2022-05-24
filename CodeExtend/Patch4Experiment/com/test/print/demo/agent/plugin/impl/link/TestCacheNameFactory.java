package com.test.print.demo.agent.plugin.impl.link;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;

public class TestCacheNameFactory {
    private static final Map<String, String> methodNameAndCode = new ConcurrentHashMap<>();
    private static final Map<String, AtomicLong> methodNameAndVisitCount = new ConcurrentHashMap<>();

    private static final AtomicLong ai = new AtomicLong(0);
    // private static final AtomicLong ti = new AtomicLong(0);
    // private static AtomicReferenceArray<String> arry = new AtomicReferenceArray<String>(4150000);
    private static AtomicReference<String> str = new AtomicReference<String>("");
    public static String getMethodCode(String methodName) {
        String code = methodNameAndCode.computeIfAbsent(methodName, x -> "M" + ai.addAndGet(1));
        AtomicLong atomicLong = methodNameAndVisitCount.computeIfAbsent(methodName, x -> new AtomicLong(0));
        // arry.set((int)ti.get(),code);
        AtomicReference<String> a = new AtomicReference<String>(code);
        str.set(str.get() + a.get());
        // ti.addAndGet(1);
        atomicLong.addAndGet(1);
        
        return code;
    }

    // public static AtomicInteger getNum(){
    //     return ti;
    // }

    public static String printArry(){
        // String ans = new String();
        // for (int i=0;i<ti.get();i++){
        //     ans = ans + arry.get(i) + "\n";
        // }
        // return ans;
        return str.get();
    }

    public static Map<String, String> getCacheMapping() {
        return methodNameAndCode;
    }

    public static Map<String, AtomicLong> getMappingVisitCount() {
        return methodNameAndVisitCount;
    }

    public static Long getMappingVisitCountbyMethod(String methodName) {
        AtomicLong atomicLong = methodNameAndVisitCount.computeIfAbsent(methodName, x -> new AtomicLong(0));
        Long MethodCount = atomicLong.get();
        return MethodCount;
    }

    public static void main(String[] args) {
        String methodCode = TestCacheNameFactory.getMethodCode("aClass.aMethod");
        String methodCode2 = TestCacheNameFactory.getMethodCode("aClass.aMethod");
        String methodCode3 = TestCacheNameFactory.getMethodCode("aClass.bMethod");
        System.out.println("methodCode:" + methodCode);
        System.out.println("methodCode2:" + methodCode2);
        System.out.println("methodCode3:" + methodCode3);
        System.out.println("mapping:" + TestCacheNameFactory.getCacheMapping());
        System.out.println("mapping-count:" + TestCacheNameFactory.getMappingVisitCount());
    }
}
