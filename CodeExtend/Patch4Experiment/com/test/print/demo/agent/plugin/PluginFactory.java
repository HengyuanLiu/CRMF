package com.test.print.demo.agent.plugin;

import com.test.print.demo.agent.plugin.impl.link.LinkPlugin;

import java.util.ArrayList;
import java.util.List;

/**
 * 博客：http://itstack.org
 * 论坛：http://bugstack.cn
 * 公众号：bugstack虫洞栈  ｛获取学习源码｝
 * create by fuzhengwei on 2019
 */
public class PluginFactory {

    public static List<IPlugin> pluginGroup = new ArrayList<>();

    static {
        //链路监控
        pluginGroup.add(new LinkPlugin());
    }

}
