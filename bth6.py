<?xml version="1.0"?>
<flowgorithm fileversion="2.11">
    <attributes>
        <attribute name="name" value=""/>
        <attribute name="authors" value="Administrator"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2020-03-25 08:37:48 AM"/>
        <attribute name="created" value="QWRtaW5pc3RyYXRvcjs2UzQ3UzVEMTM3U0VYRzE7MjAyMC0wMy0xNzsxMDozMToyMiBBTTszNTkz"/>
        <attribute name="edited" value="QWRtaW5pc3RyYXRvcjs2UzQ3UzVEMTM3U0VYRzE7MjAyMC0wMy0yNTswODozNzo0OCBBTTs1OzM3MjU="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <comment text=""/>
            <declare name="n" type="Integer" array="False" size=""/>
            <for variable="n" start="99" end="1" direction="dec" step="1">
                <if expression="n==1">
                    <then>
                        <output expression="&quot;one bottle of beer on the wall&quot;" newline="True"/>
                    </then>
                    <else>
                        <output expression="&quot;bottles of beer on the wall&quot;" newline="True"/>
                    </else>
                </if>
            </for>
        </body>
    </function>
</flowgorithm>
