fp = open("../../gson/pom.xml", mode='r')
pom = fp.readlines()
fp.close()

def pom_finder(start_str, end_str, start_loc, end_loc):
    start_find_flag = False
    end_find_flag = False
    for i in range(start_loc, end_loc):
        if start_str in pom[i]:
            start_find_flag = True
        elif end_str in pom[i]:
            end_find_flag = True
            break
    return start_find_flag and end_find_flag

def pom_locator(start_str, end_str, start_loc, end_loc):
    start_flag = 0
    end_flag = 0
    for i in range(start_loc, end_loc):
        if start_str in pom[i]:
            start_flag = i
        elif end_str in pom[i]:
            end_flag = i
            break
    return start_flag, end_flag

# unify the SNAPSHOT name
snapshot_hint = False 
for i in range(len(pom)):
    if "-SNAPSHOT</version>" in pom[i]:
        pom[i] = "<version>0.0-SNAPSHOT</version>\n"
        snapshot_hint = True
        break
# not snapshot exist
if not snapshot_hint:
    for i in range(len(pom)):
        if "</version>" in pom[i]: 
            pom[i] = "<version>0.0-SNAPSHOT</version>\n"
            break

for i in range(len(pom)):
    if "<maven.compile.source>" in pom[i]:
        pom[i] = "<maven.compile.source>1.8</maven.compile.source>\n"
        break
    if "<maven.compiler.source>" in pom[i]:
        pom[i] = "<maven.compiler.source>1.8</maven.compiler.source>\n"
        break

for i in range(len(pom)):
    if "<maven.compile.target>" in pom[i]:
        pom[i] = "<maven.compile.target>1.8</maven.compile.target>\n"
        break
    if "<maven.compiler.target>" in pom[i]:
        pom[i] = "<maven.compiler.target>1.8</maven.compiler.target>\n"
        break

dependencies_finder = pom_finder("<dependencies>","</dependencies>",0,len(pom))
properties_finder = pom_finder("<properties>","</properties>",0,len(pom))
if dependencies_finder:
    dependencies_start, dependencies_end = pom_locator("<dependencies>","</dependencies>",0,len(pom))
    if properties_finder:
        # print("Have properties")
        for i in range(len(pom)):
            if "</properties>" in pom[i]:
                pom[i] = """
            <!-- 自定义MANIFEST.MF -->
            <maven.configuration.manifestFile>src/main/resources/META-INF/MANIFEST.MF</maven.configuration.manifestFile>
            </properties>
            """    
                break
    else:
        # print("No properties")
        # print(pom[dependencies_start])
        pom.insert(dependencies_start, """
        <properties>
        <!-- 自定义MANIFEST.MF -->
        <maven.configuration.manifestFile>src/main/resources/META-INF/MANIFEST.MF</maven.configuration.manifestFile>
        </properties>
        """)
        # print(pom[dependencies_start])
    

junit_flag=False
dependencies_start, dependencies_end = pom_locator("<dependencies>","</dependencies>",0,len(pom))
for locator in range(dependencies_start,dependencies_end):
    dependency_start, dependency_end = pom_locator("<dependency>","</dependency>",locator,dependencies_end)
    for i in range(dependency_start, dependency_end):
        if "junit" in pom[i]:
            junit_flag = True
    if junit_flag:
        pom[dependency_start:dependency_end+1] = []
        break

dependencies_start, dependencies_end = pom_locator("<dependencies>","</dependencies>",0,len(pom))
pom[dependencies_start] = """
<dependencies>
        <dependency>
          <groupId>junit</groupId>
          <artifactId>junit</artifactId>
          <version>4.12</version>
        </dependency>
        <dependency>
            <groupId>javassist</groupId>
            <artifactId>javassist</artifactId>
            <version>3.12.1.GA</version>
            <type>jar</type>
        </dependency>
        <dependency>
            <groupId>net.bytebuddy</groupId>
            <artifactId>byte-buddy</artifactId>
            <version>1.8.20</version>
        </dependency>
        <dependency>
            <groupId>net.bytebuddy</groupId>
            <artifactId>byte-buddy-agent</artifactId>
            <version>1.8.20</version>
        </dependency>
        <dependency>
          <groupId>org.apache.felix</groupId>
          <artifactId>maven-bundle-plugin</artifactId>
          <version>2.5.3</version>
        </dependency>
"""

build_start, build_end = pom_locator("<build>","</build>",0,len(pom))
if pom_finder("<pluginManagement>","</pluginManagement>",build_start,build_end):
    pluginManagement_start, pluginManagement_end = pom_locator("<pluginManagement>","</pluginManagement>",build_start,build_end)
    plugins_start, plugins_end = pom_locator("<plugins>","</plugins>",pluginManagement_end,build_end)
else:
    plugins_start, plugins_end = pom_locator("<plugins>","</plugins>",build_start,build_end)

# head=plugins_start
# tail=plugins_end
head=0
tail=len(pom)-1
checkover = False
while not checkover:
    indicator = pom_finder("<plugin>","</plugin>",head,tail)
    # print(''.join(pom[head:tail+1]))
    # print("Checking")
    # print(head, tail)
    # print(indicator)
    if indicator:
        plugin_start, plugin_end = pom_locator("<plugin>","</plugin>",head,tail)
        # print("Indicate", plugin_start, plugin_end)
        for i in range(plugin_start, plugin_end+1):
            if "maven-compiler-plugin" in pom[i]:
                # print("find compiler")
                for i in range(plugin_start, plugin_end+1):
                    if "<source>" in pom[i]:
                        # print("find source version")
                        pom[i] = "<source>1.8</source>\n"
                        # print(pom[i])
                        break
                for i in range(plugin_start, plugin_end+1):
                    if "<target>" in pom[i]:
                        # print("find target version")
                        pom[i] = "<target>1.8</target>\n"
                        # print(pom[i])
                        break
            if "maven-jar-plugin" in pom[i]:
                # print("find jar plugin")
                for i in range(plugin_start, plugin_end+1):
                    pom[i] = "\n"
        head = plugin_end+1
    else:
        checkover = True
    
pom[plugins_start] = """
<plugins>
      <plugin>
        <!-- 将javassist包打包到Agent中 -->
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <version>2.4.3</version>
        <!-- <configuration>
            <createDependencyReducedPom>false</createDependencyReducedPom>
        </configuration> -->
        <executions>
            <execution>
                <phase>package</phase>
                <goals>
                    <goal>shade</goal>
                </goals>
            </execution>
        </executions>
        <configuration>
            <artifactSet>
                <includes>
                    <include>javassist:javassist:jar:</include>
                    <include>net.bytebuddy:byte-buddy:jar:</include>
                    <include>net.bytebuddy:byte-buddy-agent:jar:</include>
                </includes>
            </artifactSet>
        </configuration>
      </plugin>
      <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-jar-plugin</artifactId>
          <version>3.1.0</version>
          <configuration>
              <archive>
                  <manifestFile>src/main/resources/META-INF/MANIFEST.MF</manifestFile>
              </archive>
          </configuration>
      </plugin>
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <version>2.5.3</version>
        <dependencies>
          <dependency>
            <groupId>biz.aQute.bnd</groupId>
            <artifactId>bndlib</artifactId>
            <version>2.4.0</version>
          </dependency>
        </dependencies>
      </plugin> 
"""


# print(''.join(pom))
fp = open("../../gson/pom.xml", mode='w')
fp.write(''.join(pom))
fp.close()

import os

if os.path.exists("../../pom.xml"):
    fp = open("../../pom.xml", mode='r')
    pom = fp.readlines()
    fp.close()

    # unify the SNAPSHOT name
    snapshot_hint = False 
    for i in range(len(pom)):
        if "-SNAPSHOT</version>" in pom[i]:
            pom[i] = "<version>0.0-SNAPSHOT</version>\n"
            snapshot_hint = True
            break
    # not snapshot exist
    if not snapshot_hint:
        for i in range(len(pom)):
            if "</version>" in pom[i]: 
                pom[i] = "<version>0.0-SNAPSHOT</version>\n"
                break
    
    for i in range(len(pom)):
        if "<java.version>" in pom[i]:
            pom[i] = "<java.version>1.8</java.version>\n"
    
head=0
tail=len(pom)-1
checkover = False
while not checkover:
    indicator = pom_finder("<plugin>","</plugin>",head,tail)
    # print(''.join(pom[head:tail+1]))
    # print("Checking")
    # print(head, tail)
    # print(indicator)
    if indicator:
        plugin_start, plugin_end = pom_locator("<plugin>","</plugin>",head,tail)
        # print("Indicate", plugin_start, plugin_end)
        for i in range(plugin_start, plugin_end+1):
            if "maven-compiler-plugin" in pom[i]:
                # print("find compiler")
                for i in range(plugin_start, plugin_end+1):
                    if "<source>" in pom[i]:
                        # print("find source version")
                        pom[i] = "<source>1.8</source>\n"
                        # print(pom[i])
                        break
                for i in range(plugin_start, plugin_end+1):
                    if "<target>" in pom[i]:
                        # print("find target version")
                        pom[i] = "<target>1.8</target>\n"
                        # print(pom[i])
                        break
            if "maven-jar-plugin" in pom[i]:
                # print("find jar plugin")
                for i in range(plugin_start, plugin_end+1):
                    pom[i] = "\n"
        head = plugin_end+1
    else:
        checkover = True

fp = open("../../pom.xml", mode='w')
fp.write(''.join(pom))
fp.close()