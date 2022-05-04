
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
import axios from 'axios';
import PageOne from './pages/PageOne';



function App() {
  const { Option } = Select;
  const { TextArea } = Input;
  const { Header, Sider, Content } = Layout;
  const {Meta} = Card;
  const [displayPage, setDisplayPage] = useState('home');
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
            <Menu.Item key="1" onClick ={() =>{setDisplayPage('home');}} icon={<HomeOutlined size={18}></HomeOutlined>}>Page1</Menu.Item>
            <Menu.Item key="2" onClick ={() =>{setDisplayPage('friend');}} icon={<UserOutlined size={18} ></UserOutlined>}>Page2</Menu.Item>
            <Menu.Item key="3" onClick ={() =>{setDisplayPage('message')}} icon={<BellOutlined size={18} ></BellOutlined>}>Page3</Menu.Item>
            <Menu.Item key="4" onClick ={() =>{setDisplayPage('planet')}} icon={<RocketOutlined size={18} />}>Page4</Menu.Item>
        </Menu>
        {displayPage === 'home'?<PageOne></PageOne>:null}
      

    </div>
  );
}

export default App;
