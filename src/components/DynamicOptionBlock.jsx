// React
import React, { Component } from 'react';

// React-Bootstrap
import ToggleButton from 'react-bootstrap/ToggleButton';
import ToggleButtonGroup from 'react-bootstrap/ToggleButtonGroup';

// Local
import DynamicBlock from './DynamicBlock.jsx';

export default class DynamicOptionBlock extends Component {
    render() {
        const options = Object.keys(this.props.options)
            .map((option) => (
                <ToggleButton
                    className="toggle-button-no-border noshadow"
                    style={this.props.buttonStyle}
                    variant={this.props.value == option
                        ? 'success active'
                        : 'light'}
                    type='radio'
                    value={option}
                    name='options'
                    key={option}
                >
                    {option}
                </ToggleButton>
            ));

        const buttonGroup = (
            <ToggleButtonGroup
                // className='pb-2'
                name={this.props.name}
                style={this.props.buttonGroupStyle}
                className={this.props.buttonGroupClass}
                type='radio'
                onChange={
                    (option) => {
                        this.props.onChangeFunc(option);
                    }}
                value={this.props.value}
            >
                {options}
            </ToggleButtonGroup>
        );

        const blockRenderCallback = (function (name) {
            return name == this.props.value;
        }).bind(this);

        const blocks = Object.entries(this.props.options)
            .map(([name, block]) => {
                return (
                    <DynamicBlock key={name} name={name} callback={blockRenderCallback}>
                        {block}
                    </DynamicBlock>
                )
            });

        const optionBlock = (

            <div className={this.props.className}>
                {buttonGroup}
                {blocks}
            </div>
        );

        return optionBlock;
    }
}