import React, { Component } from 'react'
import '../src/css/table.scss'


class Tbl extends Component {
    render() {
        return (
            <table className="data-table">
                <thead>
                    <tr>
                        <th>id</th>
                        <th>名称</th>
                        <th>标题</th>
                        <th>网址</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>今天</td>
                        <td>是不是很好</td>
                        <td>http://www/so/com</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>今天</td>
                        <td>是不是很好</td>
                        <td>http://www/so/com</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>今天</td>
                        <td>是不是很好</td>
                        <td>http://www/so/com</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>今天</td>
                        <td>是不是很好</td>
                        <td>http://www/so/com</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>今天</td>
                        <td>是不是很好</td>
                        <td>http://www/so/com</td>
                    </tr>
                    <tr>
                        <td>1</td>
                        <td>今天</td>
                        <td>是不是很好</td>
                        <td>http://www/so/com</td>
                    </tr>
                </tbody>
            </table>
        )
    }
}

export default Tbl