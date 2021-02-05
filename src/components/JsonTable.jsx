import React, { Component } from 'react';

class JsonTable extends Component {

    constructor(props) {
        super(props);
        this.getHeader = this.getHeader.bind(this);
        this.getRowsData = this.getRowsData.bind(this);
        this.getKeys = this.getKeys.bind(this);
    }

    getKeys = function () {
        return Object.keys(this.props.data[0]);
    }

    getHeader = function () {
        var keys = this.getKeys();
        return keys.map((key, index) => {
            var clean_key = key;
            return <th key={index} onClick={() => this.props.sortBy(key)}>{clean_key.toUpperCase()}</th>
        })
    }

    getRowsData = function () {
        var items = this.props.data;
        var keys = this.getKeys();
        return items.map((row, index) => {
            return <tr key={index} id={this.props.className}><RenderRow key={index} data={row} keys={keys} /></tr>
        })
    }

    render() {
        if (this.props.data === null) {
            return (null);
        } else {
            return (
                <div>
                    <table id='work'>
                        <thead>
                            {this.props.extraHeader}
                            <tr id={this.props.className}>{this.getHeader()}</tr>
                        </thead>
                        <tbody>
                            {this.getRowsData()}
                        </tbody>
                    </table>
                </div>

            );
        };
    }
}
const RenderRow = (props) => {
    return props.keys.map((key, index) => {
        return <td key={index}>{props.data[key]}</td>
    })
}

export { JsonTable };
