package com.test.print.demo.agent;

import com.test.print.demo.agent.plugin.IPlugin;
import com.test.print.demo.agent.plugin.InterceptPoint;
import com.test.print.demo.agent.plugin.PluginFactory;
import net.bytebuddy.agent.builder.AgentBuilder;
import net.bytebuddy.asm.Advice;
import net.bytebuddy.description.type.TypeDescription;
import net.bytebuddy.dynamic.DynamicType;
import net.bytebuddy.utility.JavaModule;

import java.lang.instrument.Instrumentation;
import java.util.List;
import java.lang.Runtime;

import com.test.print.demo.agent.plugin.impl.link.TestCacheNameFactory;
/**
 * 博客：http://itstack.org
 * 论坛：http://bugstack.cn
 * 公众号：bugstack虫洞栈  ｛获取学习源码｝
 * create by fuzhengwei on 2019
 */

// static {
//         Runtime.getRuntime().addShutdownHook(new Thread(() -> {
//             System.out.println("mapping:" + TestCacheNameFactory.getCacheMapping());
//             System.out.println("mapping-count:" + TestCacheNameFactory.getMappingVisitCount());
//         }));
//     }

public class MyAgent {

    //JVM 首先尝试在代理类上调用以下方法
    public static void premain(String agentArgs, Instrumentation inst) {
        // System.out.println("------------------------------------------");
        // System.out.println("Enter MyAgent.java premain");
        // System.out.println("------------------------------------------");


        TestCacheNameFactory temp= new TestCacheNameFactory();

        Runtime.getRuntime().addShutdownHook(new Thread(() -> System.out.println(temp.getCacheMapping()+"\n\n"+temp.getMappingVisitCount() )));
        
        
        AgentBuilder agentBuilder = new AgentBuilder.Default();

        List<IPlugin> pluginGroup = PluginFactory.pluginGroup;
        for (IPlugin plugin : pluginGroup) {

            // System.out.println("------------------------------------------");
            // System.out.println(plugin);
            // System.out.println("------------------------------------------");

            InterceptPoint[] interceptPoints = plugin.buildInterceptPoint();
            for (InterceptPoint point : interceptPoints) {

                // System.out.println("------------------------------------------");
                // System.out.println(point);
                // System.out.println("------------------------------------------");

                AgentBuilder.Transformer transformer = (builder, typeDescription, classLoader, javaModule) -> {
                    builder = builder.visit(Advice.to(plugin.adviceClass()).on(point.buildMethodsMatcher()));
                    return builder;
                };
                agentBuilder = agentBuilder.type(point.buildTypesMatcher()).transform(transformer).asDecorator();
            }
        }
       
        // System.out.println("------------------------------------------");
        // System.out.println("Start MyAgent.java Listener");
        // System.out.println("------------------------------------------");

        //监听
        AgentBuilder.Listener listener = new AgentBuilder.Listener() {
            @Override
            public void onDiscovery(String s, ClassLoader classLoader, JavaModule javaModule, boolean b) {

            }

            @Override
            public void onTransformation(TypeDescription typeDescription, ClassLoader classLoader, JavaModule javaModule, boolean b, DynamicType dynamicType) {
                // System.out.println("onTransformation:" + typeDescription);
            }

            @Override
            public void onIgnored(TypeDescription typeDescription, ClassLoader classLoader, JavaModule javaModule, boolean b) {
                // System.out.println("onIgnored:" + typeDescription);
            }

            @Override
            public void onError(String s, ClassLoader classLoader, JavaModule javaModule, boolean b, Throwable throwable) {

            }

            @Override
            public void onComplete(String s, ClassLoader classLoader, JavaModule javaModule, boolean b) {

            }

        };
        
        agentBuilder.with(listener).installOn(inst);

        // System.out.println("------------------------------------------");
        // System.out.println("End MyAgent.java Listener");
        // System.out.println("------------------------------------------");

    }

}
