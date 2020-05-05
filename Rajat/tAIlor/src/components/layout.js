import React from 'react';
import { Layout, Menu } from 'antd';
import {Link} from 'gatsby';

const {Header, Content, Footer} = Layout;

export default ({children}) => (<Layout style={{minHeight: "100vh"}}>
    <Header>
        <Menu theme="dark" mode="horizontal" style={{
                display: "flex",
                alignItems:"flex-end",
                justifyContent:"center",
                height: "100%"
            }} selectedKeys={null}>
                <Menu.Item >
                    <h1 style={{color:"#eee"}}>t<span style={{color:"#f11"}}>AI</span>lor</h1>
                </Menu.Item>
            
        </Menu>
    </Header>
    <Content>
        {children}
    </Content>
    <Footer style={{textAlign:"center",backgroundColor: "#333",color:"#eee",padding:"1em 0.5em"}}>
        @tAIlor
    </Footer>
</Layout>)