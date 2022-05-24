package com.test.print.demo.agent.plugin.impl.link;

import com.test.print.demo.agent.track.Span;
import com.test.print.demo.agent.track.TrackContext;
import com.test.print.demo.agent.track.TrackManager;
import net.bytebuddy.asm.Advice;
// import java.io.File;
// import java.io.FileWriter;
// import java.io.IOException;
// import java.io.BufferedWriter;

import java.util.UUID;
import java.util.Arrays;

import com.test.print.demo.agent.plugin.impl.link.TestCacheNameFactory;


/**
 * 博客：http://itstack.org
 * 论坛：http://bugstack.cn
 * 公众号：bugstack虫洞栈  ｛获取学习源码｝
 * create by fuzhengwei on 2019
 */
public class LinkAdvice {

 // 

    @Advice.OnMethodEnter()
    public static void enter(@Advice.Origin java.lang.reflect.Method method, @Advice.Origin("#t") String className, @Advice.Origin("#m") String methodName) {
        
        // File file = new File("outTest.txt");
        // BufferedWriter out = new BufferedWriter(new FileWriter(file,true));
        // out.write("className:"+className+"-"+methodName+" 开始测试"+"\n");
        // out.close();
        // System.out.println("className:"+className+"-"+methodName+"####TEST####");

        Span currentSpan = TrackManager.getCurrentSpan();
        if (null == currentSpan) {
            String linkId = UUID.randomUUID().toString();
            TrackContext.setLinkId(linkId);
        }
        TrackManager.createEntrySpan();
    }

 
    @Advice.OnMethodExit()
    public static void exit(@Advice.Origin java.lang.reflect.Method method,@Advice.Origin("#t") String className, @Advice.Origin("#m") String methodName){
         

        // File file = new File("outTest.txt");
        // BufferedWriter bw=null;
        // bw = new BufferedWriter(new FileWriter(file,true));
       
        Span exitSpan = TrackManager.getExitSpan();
        if (null == exitSpan) return;
        // bw.write(className + "." + methodName +"\n");
        TestCacheNameFactory t = new TestCacheNameFactory();
       

        // ti.addAndGet(1);
        
        // int ti = (int) t.getNum();
        // System.out.println(ti);
        // temp[ti] = ;

        // test
        if (t.getMappingVisitCountbyMethod(className + "." + methodName) < 10000) {
            t.getMethodCode(className + "." + methodName);
        } 

        // // debug
        // System.out.println("-------------------------------------------------------");
        // System.out.println(className + "." + methodName + "!!!!!!!!!!!!!!!!!!!!!!!!");
        // // System.out.println(t.getMappingVisitCount());
        // System.out.println("Before:" + t.getMappingVisitCountbyMethod(className + "." + methodName));
        // // System.out.println("-------------------------------------------------------");
        // if (t.getMappingVisitCountbyMethod(className + "." + methodName) < 1000) {
        //     t.getMethodCode(className + "." + methodName);
        // } 
        // // System.out.println("-------------------------------------------------------");
        // System.out.println(className + "." + methodName + "????????????????????????");
        // // System.out.println(t.getMappingVisitCount());
        // System.out.println("After: " + t.getMappingVisitCountbyMethod(className + "." + methodName));
        // System.out.println("-------------------------------------------------------");

        // if (method.isAnnotationPresent(org.junit.Test.class)){
        //     System.out.println("test " + t.getNum());
        //     // System.out.println(temp[ti]);
        // }
        

        // bw.write(temp+"\n");

        // // bw.write("className:"+className+"-"+methodName+" 结束测试"+"\n");
        // // System.out.println("链路追踪(MQ)：" + exitSpan.getLinkId() + " " + className + "." + methodName + " 耗时：" + (System.currentTimeMillis() - exitSpan.getEnterTime().getTime()) + "ms");
        // // System.out.println("className:"+className+"-"+methodName+"结束测试");
        // bw.close();
        
    }

}


