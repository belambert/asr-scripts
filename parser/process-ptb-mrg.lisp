(declaim (optimize (debug 3)))

(defun read-ptb-mrg (filename)
  (let ((sentences '()))
    (with-open-file (f filename)
      (loop for form = (read f nil nil)
	   while form do
	   (push form sentences)))
    (nreverse sentences)))

(defun count-parens (filename)
  (let ((lp 0)
	(rp 0))
    (with-open-file (f filename)
      (loop for line = (read-line f nil nil)
	   while line do
	   (incf lp (count #\( line))
	   (incf rp (count #\) line))
	   (format t "~d ~d ~d~%" lp rp (- lp rp))
	   ))
    (list lp rp)))

(defun find-in-tree (e tree &key (test 'eql))
  (if (atom tree)
      (if (funcall test e tree)
	  (return-from find-in-tree tree)
	  (return-from find-in-tree nil))
      (some (lambda (subtree) (find-in-tree e subtree)) tree)))

(defun remove-layer-from-tree (target tree &key (test 'eql))
  (loop for e in tree
       append
       (cond ((atom e)
	      (list e))
	     ((funcall test target (car e))
	      (remove-layer-from-tree target (cdr e) :test test))
	     (t
	      (list (remove-layer-from-tree target e :test test))))))

(defun remove-subtree-from-tree (subtree tree)
  (loop for e in tree
       append
       (cond ((tree-equal e subtree)
	      nil)
	     ((atom e)
	      (list e))
	     (t
	      (list (remove-subtree-from-tree subtree e))))))

(defun write-trees-to-file (trees filename)
  (with-open-file (s filename :if-exists :supersede :if-does-not-exist :create :direction :output)
    (dolist (tree trees)
      (princ tree s)
      (terpri s))))

(defun remove-edited-layers (tree)
  (remove-layer-from-tree 'EDITED tree))

(defparameter *disfluency-list*
  '(UM
    UH
    MM
    AH
    ER
    EH
    EH-
    MHM
    HM
    HA
    HUH
    UH-HUH))

(defun remove-disfluencies (tree)
  (dolist (disfluency *disfluency-list*)
    (let ((subtree `(INTJ (UH ,disfluency))))
      (setf tree (remove-subtree-from-tree subtree tree))))
  tree)

(defun cleanup-trees (trees)
  ;; The functions I wrote shouldn't be destructive, but make copies, just in case
  (setf trees (mapcar 'copy-tree trees))
  (setf trees (mapcar 'remove-edited-layers trees))
  (setf trees (mapcar 'remove-disfluencies trees))
  (setf trees (remove-if 'null trees))
  (setf trees (remove '((INTJ)) trees :test 'equalp)))

(defun split-mrg-file (orig file1 file2)
  (let* ((sentences (read-ptb-mrg orig))
	 (length (length sentences))
	 (middle (ceiling (/ length 2)))
	 (train (subseq sentences 0 middle))
	 (test (subseq sentences middle)))
    (write-trees-to-file train file1)
    (write-trees-to-file test file2)))






	
