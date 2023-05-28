import { connect } from 'react-redux';

function Layout({children}){
    return (
        <div className="flex h-screen">
            {children}
        </div>
    )
}

const mapStateToProps = state =>({

})

export default connect(mapStateToProps,{})(Layout);