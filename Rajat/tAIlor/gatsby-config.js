/**
 * Configure your Gatsby site with this file.
 *
 * See: https://www.gatsbyjs.org/docs/gatsby-config/
 */
const path = require(`path`)

module.exports = {
  proxy:[
    {
      prefix: "/dinesh",
      url:"http://34.87.150.173"
    },
  ],
  /* Your site config here */
  plugins: [
    "gatsby-plugin-antd",
    {
      resolve: `gatsby-plugin-typography`,
      options: {
        pathToConfigModule: `src/utils/typography`,
      },
    },
    {
      resolve: "gatsby-source-filesystem",
      options: {
        name: "designs",
        path: path.join(__dirname,'static')
      }
    },
    `gatsby-plugin-sharp`,
    `gatsby-transformer-sharp`
  ],
}
