<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Dropbox</h2>
  <ul>
    <li><h4>User-info:</h4><xsl:value-of select="dropbox/metadata/user"/></li>
    <li><h4>Course-info:</h4><xsl:value-of select="dropbox/metadata/course"/></li>
    <li><h4>File generated on:</h4><xsl:value-of select="dropbox/metadata/date"/></li>
  </ul>
  <table border="1">
    <tr bgcolor="#9acd32">
        <th>File</th>
        <th>Author</th>
        <th>Description</th>
        <th>Date Published</th>
    </tr>
    <xsl:for-each select="dropbox/item">
    <tr>
        <td>
            <a>
                <xsl:attribute name="href">
                    <xsl:value-of select="file" />
                </xsl:attribute>
                <xsl:value-of select="file" />
            </a>
        </td>
        <td><xsl:value-of select="author"/></td>
        <td><xsl:value-of select="description"/></td>
        <td><xsl:value-of select="post_date"/></td>
   </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
