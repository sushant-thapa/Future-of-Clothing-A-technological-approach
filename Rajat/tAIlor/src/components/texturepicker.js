import React from 'react';

import {graphql,useStaticQuery} from 'gatsby';
import { Row,Col, Button } from 'antd';

import {RobotOutlined,UploadOutlined} from '@ant-design/icons';

import Img from 'gatsby-image';

import '../../static/css/texturepicker.css';

export default ({textureState}) => {
    const data = useStaticQuery(graphql`
    query {
        allFile {
            edges {
                node {
                    childImageSharp {
                        fluid {
                        ...GatsbyImageSharpFluid
                        }
                    }
                }
            }
        }
    }`);


    const [texture,setTexture] = textureState;
    const designs = data.allFile.edges;

    console.log(designs[0]);


    return (
        <div style={{width: "100%"}}>
            <Row style={{borderBottom:"1px black solid",height: "70%",width:"100%",}}>
                <div style={{display: "flex",justifyContent:"center",width:"100%",padding: "1.5em 1em 0em 1em"}}>
                    <img src={texture} style={{height: "300px",width: "300px",margin:"0"}}/>
                </div>
            </Row>
            <Row style={{height: "30%"}}>
                <Col span={8} style={{height: "100%", borderRight: "1px black solid"}}>
                    <Row style={{height: "50%",borderBottom: "1px black solid",display:"flex",justifyContent:"center",alignItems:"center"}}>
                        <Button size="large" type="primary" shape="round" icon={<RobotOutlined/>}>Generate</Button>
                    </Row>
                    <Row style={{height: "50%", display:"flex",justifyContent:"center",alignItems:"center"}}>
                        <Button size="large" type="primary" shape="round" icon={<UploadOutlined/>}>Upload</Button>
                    </Row>
                </Col>
                <Col span={16} style={{height: "100%"}}>
                    <ul className="imageSelector">
                        {designs.map( (design,index) => ( <li key={index} className={ (design.node.childImageSharp.fluid.src == texture) ? "selectedImage" : null}
                                onClick={() => setTexture(design.node.childImageSharp.fluid.src)}>
                                <Img fluid={design.node.childImageSharp.fluid} style={{height:"100%"}}/>
                            </li>
                        ))}
                    </ul>
                </Col>
            </Row>
        </div>
    )
}