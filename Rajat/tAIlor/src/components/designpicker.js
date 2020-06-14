import React from 'react';
import {Row , Col,Button} from 'antd';
import Img from 'gatsby-image';

import {RobotOutlined,UploadOutlined} from '@ant-design/icons';

const unflatten = ([...arr],size) => {
    const new_arr = [[]];
    for(const item of arr){
        if(new_arr[new_arr.length-1].length == size ){
            new_arr.push([]);
        }
        new_arr[new_arr.length-1].push(item);
    }
    console.log(arr,new_arr);
    return new_arr;
}

export default ({designs,designState}) => {
    const [design,setDesign] = designState;

    const generateDesign = async () => {
        const resp = await fetch('/dinesh/generate?redirect=False');
        const pathToDesign = (await resp.json()).path;
        setDesign(pathToDesign);
    }

    return (
        <div style={{height:"100%",width:"100%",backgroundColor:"#FDF5DC",position:"relative"}}>
            <Row style={{display:"flex","justifyContent":"center"}}>
                <h1 style={{margin:"auto"}}>Designs</h1>
            </Row>
            <Row style={{display:"flex","justifyContent":"center",marginTop:"1em"}}>
                <img src={design} style={{width:"100%",padding:"1em"}}/>
            </Row>
            <Row style={{display:"flex","justifyContent":"center",marginTop:"1em"}}>
                <div style={{width:"100%"}}>
                    {unflatten(designs,3).map( (row,rowIndex) => (
                        <Row key={rowIndex} style={{display:"flex",justifyContent:"center"}}>
                            {row.map( (design,colIndex) => (
                                <Col key={colIndex}
                                    span={8}
                                    style={{padding:"0.5em"}}
                                    onClick={() => setDesign(design.node.childImageSharp.fluid.src)}> 
                                    <Img fluid={design.node.childImageSharp.fluid} style={{height:"100%",width:"100%"}} />
                                </Col>) )}
                        </Row>
                    ))}
                </div>
            </Row>
            <Row style={{position:"absolute",bottom:"0",right:"0",left:"0",height:"50px"}}>
                <Col span={24} style={{display:"flex",justifyContent:"center"}}>
                    <Button size="large" type="primary" shape="round" icon={<RobotOutlined/>} 
                        onClick={() => generateDesign()}
                        style={{marginRight:"1em"}}>AI</Button>  
                    <Button size="large" type="primary" shape="round" icon={<UploadOutlined/>} >Upload</Button>   
                </Col>
            </Row>
            
        </div>
    )
}