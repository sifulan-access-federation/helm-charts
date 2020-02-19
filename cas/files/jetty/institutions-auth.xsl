<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <provider>
            <xsl:apply-templates/>
        </provider>
    </xsl:template>

    <xsl:template match="auth">
        <xsl:variable name="idp" select="//attribute[@name='Shib-Identity-Provider']/@value" />
        <idp><xsl:value-of select="$idp"/></idp>
        <xsl:choose>
            <xsl:when test="$idp='https://openidp.nii.ac.jp/idp/shibboleth'">
                <id>openidp</id>
            </xsl:when>
            <xsl:when test="$idp='https://idp.rdm.nii.ac.jp/idp/shibboleth'">
                <id>tiqr</id>
            </xsl:when>
            <xsl:otherwise>
                <xsl:message terminate="yes">Error: Unknown Identity Provider '<xsl:value-of select="$idp"/>'</xsl:message>
            </xsl:otherwise>
        </xsl:choose>
                <user>
                    <username><xsl:value-of select="//attribute[@name='eppn']/@value"/></username>
                    <xsl:choose>
                        <xsl:when test="//attribute[@name='displayName']/@value != ''">
                            <fullname><xsl:value-of select="//attribute[@name='displayName']/@value"/></fullname>
                        </xsl:when>
                        <xsl:otherwise>
                            <fullname>New User (no name)</fullname>
                        </xsl:otherwise>
                    </xsl:choose>
                    <familyName/>
                    <givenName/>
                    <middleNames/>
                    <suffix/>
                    <email><xsl:value-of select="//attribute[@name='mail']/@value"/></email>
                    <groups><xsl:value-of select="//attribute[@name='isMemberOf']/@value"/></groups>
                    <eptid><xsl:value-of select="//attribute[@name='persistent-id']/@value"/></eptid>
                </user>
    </xsl:template>
</xsl:stylesheet>
