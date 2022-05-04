
import './PageTwo.css';
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




function PageTwo() {
  const { Option } = Select;
  const { TextArea } = Input;
  const { Header, Sider, Content } = Layout;
  const {Meta} = Card;
  const [displayPage, setDisplayPage] = useState('home');
  return (
    <div className='PageOne'>
      <div>
        <Button type="primary" shape="round"  size={64}>Click To Show The Results</Button>
      </div>
    </div>
  );
}

export default PageTwo;
