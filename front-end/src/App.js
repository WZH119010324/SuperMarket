
import './App.css';
import { Form, Layout, Menu,Input, Select,Modal , Button, Upload, Avatar,Card } from 'antd';
import { MenuUnfoldOutlined,
  MenuFoldOutlined,
  UserOutlined,
  VideoCameraOutlined,
  UploadOutlined, PlusOutlined,TeamOutlined, SearchOutlined, LockOutlined, HomeOutlined, ThunderboltOutlined,StarOutlined,
  BellOutlined,AppstoreOutlined,SettingOutlined, RocketOutlined} from '@ant-design/icons';
import 'antd/dist/antd.css';
import { useState, useEffect } from 'react';

const { Option } = Select;
const { TextArea } = Input;
const { Header, Sider, Content } = Layout;
const {Meta} = Card;




function App() {
  
  

  return (
    <div className='page-1'>
       <Menu
            onClick={(e) => {
              console.log('click ', e);
            }}
            style={{ width: '18%', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'space-around' }}
            defaultSelectedKeys={['1']}
            defaultOpenKeys={['sub1']}
            mode="inline"
          >
            <Menu.Item key="1"  icon={<HomeOutlined size={18}></HomeOutlined>}>HomePage</Menu.Item>
            <Menu.Item key="2"  icon={<UserOutlined size={18} ></UserOutlined>}>Friend</Menu.Item>
            <Menu.Item key="3"  icon={<BellOutlined size={18} ></BellOutlined>}>Message</Menu.Item>
            <Menu.Item key="4"  icon={<RocketOutlined size={18} />}>Planet</Menu.Item>
            <Button className='newMoment' type="primary" shape="round" >New Moment</Button>
        </Menu>
        <div className='showPage'>
        <Button className='newMoment' type="primary" shape="round" >Click To show The data</Button>
        </div>
    </div>


  );
}

export default App;