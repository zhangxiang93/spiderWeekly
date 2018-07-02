import React from 'react'
import ReactDOM from 'react-dom'

import Ipt from '../component/input.jsx'
import Tbl from '../component/table.jsx'
import '../src/css/base.scss'

ReactDOM.render(
    <div className="page">
        <div className="content">
            <div className="item">
                <Ipt name="zxxiang"/>
            </div>
            <div className="item">
                <Tbl />
            </div>
        </div>
    </div>,
    document.getElementById('page')
)
