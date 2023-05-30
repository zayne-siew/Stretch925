import Popup from "reactjs-popup";
import styles from '@/styles/EditSessionsModal.module.css'


const EditSessionsModal = ({
    setNumSessions
}) => {
    return (
        <Popup
            trigger={open => (
                <button className={styles.editButton}>Edit Sessions</button>
            )}
            position="top center"
            closeOnDocumentClick
        >
            <div className={styles.modal}>
                <h2>Select the number of pomodoro sessions you would like to complete</h2>
                <div className={styles.selectionContainer}>
                    <button className={styles.option} onClick={() => setNumSessions(1)}>1</button>
                    <button className={styles.option} onClick={() => setNumSessions(2)}>2</button>
                    <button className={styles.option} onClick={() => setNumSessions(3)}>3</button>
                    <button className={styles.option} onClick={() => setNumSessions(4)}>4</button>
                    <button className={styles.option}onClick={() => setNumSessions(5)}>5</button>
                </div>
            </div>
        </Popup>

     );
}

export default EditSessionsModal;