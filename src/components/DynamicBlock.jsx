// React 
import React, { Component } from 'react';


export default class DynamicBlock extends Component {
    render() {
        if (this.props.callback(this.props.name)) {
            return (
                <div
                    className={this.props.className}
                >
                    {this.props.children}
                </div>
            )
        }
        return null;
    }
}